import subprocess

def run_cmd(command):
    print(f"\n👉 Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def main():
    print("🚨 This will remove all unused Docker containers, images, volumes, and networks.")
    confirm = input("Are you sure you want to proceed? (y/n): ").lower()
    
    if confirm != 'y':
        print("❌ Cleanup canceled.")
        return

        # Stop and remove all containers
    run_cmd("docker rm -f $(docker ps -aq)")

    # Prune system (images, networks, etc.)
    run_cmd("docker system prune -a --volumes -f")

    # Prune volumes just in case any remain
    run_cmd("docker volume prune -f")

    # Remove all volumes, use with caution!
    run_cmd("docker volume rm $(docker volume ls -q)")
 

    # Show Docker disk usage
    run_cmd("docker system df")


    print("\n✅ Docker cleanup complete.")

if __name__ == "__main__":
    main()

