set shell := ["powershell.exe", "-c"]

[private]
default:
    @just --list

# Git:

alias gc := git-commit
alias gp := git-push
alias gcp := git-commit-push

# Docker:

alias b := build
alias d := down
alias r := restart
alias l := logs

[group("git")]
git-commit msg:
    git add *
    git commit -m "{{ msg }}"

[group("git")]
git-push:
    git push

[group("git")]
git-commit-push msg:
    git add *
    git commit -m "{{ msg }}"
    git push

[group("docker")]
build:
    docker-compose build

[group("docker")]
up:
    docker-compose up -d

[group("docker")]
watch:
    docker-compose watch

[group("docker")]
down:
    docker-compose down

[group("docker")]
restart:
    docker-compose down
    docker-compose build
    docker-compose up -d

[group("docker")]
logs:
    docker-compose logs -f

[group("db")]
migrate msg:
    docker-compose exec api alembic revision --autogenerate -m "{{ msg }}"

[group("db")]
upgrade:
    docker-compose exec api alembic upgrade head
