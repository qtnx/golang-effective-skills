#!/usr/bin/env bash
set -euo pipefail

force=0
dry_run=0
install_skills=1
install_agents=1

for arg in "$@"; do
  case "$arg" in
    --force)
      force=1
      ;;
    --dry-run)
      dry_run=1
      ;;
    --skills-only)
      install_agents=0
      ;;
    --agents-only)
      install_skills=0
      ;;
    *)
      echo "unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
skills_dir="$repo_root/skills"
agents_dir="$repo_root/agents"
codex_root="${CODEX_HOME:-$HOME/.codex}"
skills_dest="$codex_root/skills"
agents_dest="$codex_root/agents"

if [[ "$install_skills" -eq 1 && ! -d "$skills_dir" ]]; then
  echo "skills directory not found: $skills_dir" >&2
  exit 1
fi

if [[ "$install_agents" -eq 1 && ! -d "$agents_dir" ]]; then
  echo "agents directory not found: $agents_dir" >&2
  exit 1
fi

echo "Skills destination: $skills_dest"
echo "Agents destination: $agents_dest"

if [[ "$dry_run" -eq 0 ]]; then
  if [[ "$install_skills" -eq 1 ]]; then
    mkdir -p "$skills_dest"
  fi
  if [[ "$install_agents" -eq 1 ]]; then
    mkdir -p "$agents_dest"
  fi
fi

installed=0
if [[ "$install_skills" -eq 1 ]]; then
  for skill_path in "$skills_dir"/*; do
    [[ -d "$skill_path" ]] || continue
    skill_name="$(basename "$skill_path")"
    target="$skills_dest/$skill_name"

    if [[ -e "$target" && "$force" -eq 0 ]]; then
      echo "skip existing skill: $skill_name (use --force to overwrite)"
      continue
    fi

    if [[ "$dry_run" -eq 1 ]]; then
      if [[ -e "$target" && "$force" -eq 1 ]]; then
        echo "would overwrite skill: $skill_name"
      else
        echo "would install skill: $skill_name"
      fi
    else
      if [[ -e "$target" ]]; then
        rm -rf "$target"
      fi
      cp -R "$skill_path" "$target"
      echo "installed skill: $skill_name"
    fi
    installed=$((installed + 1))
  done
fi

if [[ "$install_agents" -eq 1 ]]; then
  for agent_path in "$agents_dir"/*.md; do
    [[ -f "$agent_path" ]] || continue
    agent_name="$(basename "$agent_path")"
    target="$agents_dest/$agent_name"

    if [[ -e "$target" && "$force" -eq 0 ]]; then
      echo "skip existing agent: $agent_name (use --force to overwrite)"
      continue
    fi

    if [[ "$dry_run" -eq 1 ]]; then
      if [[ -e "$target" && "$force" -eq 1 ]]; then
        echo "would overwrite agent: $agent_name"
      else
        echo "would install agent: $agent_name"
      fi
    else
      if [[ -e "$target" ]]; then
        rm -f "$target"
      fi
      cp "$agent_path" "$target"
      echo "installed agent: $agent_name"
    fi
    installed=$((installed + 1))
  done
fi

if [[ "$installed" -eq 0 ]]; then
  echo "nothing installed"
fi
