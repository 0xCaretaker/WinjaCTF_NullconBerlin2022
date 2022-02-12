### run
docker build -t evil-morty:latest .
docker run -itdp 8000:8000 --name evil-morty evil-morty:latest bash
