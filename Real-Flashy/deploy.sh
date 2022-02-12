### run
docker build -t real-flashy:latest .
docker run --tmpfs "/dev/shm:exec" -itdp 2222:22 --name real-flashy real-flashy:latest bash
