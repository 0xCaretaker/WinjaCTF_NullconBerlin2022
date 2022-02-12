### run
docker build -t magician:latest .
docker run -itdp 8080:8080 --name magician magician:latest bash
