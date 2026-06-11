#!/usr/bin/env python3
"""Stop hook: pede avaliação ao usuário se uma skill-gatilho foi usada na sessão.

A lista de skills-gatilho e o link do formulário ficam em
feedback-triggers.json (mesma pasta deste script), permitindo adicionar
novas skills sem alterar este script.
"""
import json
import os
import pathlib
import sys


def main():
    data = json.load(sys.stdin)

    if data.get("stop_hook_active"):
        return

    cwd = pathlib.Path(data.get("cwd", os.getcwd()))
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path")

    config_path = pathlib.Path(__file__).parent / "feedback-triggers.json"
    if not config_path.exists():
        return

    config = json.loads(config_path.read_text())
    trigger_skills = set(config.get("trigger_skills", []))
    form_url = config.get("form_url")
    if not trigger_skills or not form_url:
        return

    state_dir = cwd / ".claude" / ".feedback-state"
    state_dir.mkdir(parents=True, exist_ok=True)
    marker = state_dir / f"{session_id}.done"
    if marker.exists():
        return

    if not transcript_path or not os.path.exists(transcript_path):
        return

    used_skills = set()
    with open(transcript_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            content = entry.get("message", {}).get("content")
            if not isinstance(content, list):
                continue

            for block in content:
                if (
                    isinstance(block, dict)
                    and block.get("type") == "tool_use"
                    and block.get("name") == "Skill"
                ):
                    skill_name = block.get("input", {}).get("skill")
                    if skill_name in trigger_skills:
                        used_skills.add(skill_name)

    if not used_skills:
        return

    marker.write_text(",".join(sorted(used_skills)))

    reason = (
        "Antes de finalizar esta resposta, adicione ao final uma mensagem curta "
        "e não intrusiva convidando o usuário a preencher a pesquisa de "
        f"avaliação neste link: {form_url}\n"
        "Não repita esse convite em respostas futuras desta sessão."
    )
    print(json.dumps({"decision": "block", "reason": reason}))


if __name__ == "__main__":
    main()
