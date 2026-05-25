import heapq

# JOB CLASS
class Job:
    def __init__(self, job_id, job_name, priority):
        self.job_id = job_id
        self.job_name = job_name
        self.priority = priority

    # Compare priorities for heap
    def __lt__(self, other):
        return self.priority < other.priority


# JOB SCHEDULER CLASS
class JobScheduler:
    def __init__(self):
        self.job_queue = []

    # Add Job
    def add_job(self, job_id, job_name, priority):
        job = Job(job_id, job_name, priority)
        heapq.heappush(self.job_queue, job)
        print("\nJob added successfully!")

    # Execute Highest Priority Job
    def execute_job(self):
        if not self.job_queue:
            print("\nNo jobs available!")
        else:
            job = heapq.heappop(self.job_queue)
            print(f"\nExecuting Job:")
            print(f"Job ID: {job.job_id}")
            print(f"Job Name: {job.job_name}")
            print(f"Priority: {job.priority}")

    # Display All Jobs
    def display_jobs(self):
        if not self.job_queue:
            print("\nNo jobs in queue!")
        else:
            print("\n------ JOBS IN QUEUE ------")

            # Sort for display purpose only
            sorted_jobs = sorted(self.job_queue)

            for job in sorted_jobs:
                print(f"ID: {job.job_id} | "
                      f"Name: {job.job_name} | "
                      f"Priority: {job.priority}")

    # Remove Job by ID
    def remove_job(self, job_id):
        found = False

        for job in self.job_queue:
            if job.job_id == job_id:
                self.job_queue.remove(job)
                heapq.heapify(self.job_queue)
                found = True
                print("\nJob removed successfully!")
                break

        if not found:
            print("\nJob ID not found!")


# MAIN PROGRAM
scheduler = JobScheduler()

while True:

    print("\n========== PRIORITY JOB SCHEDULER ==========")
    print("1. Add Job")
    print("2. Execute Job")
    print("3. Display Jobs")
    print("4. Remove Job")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        # ADD JOB
        if choice == 1:
            job_id = int(input("Enter Job ID: "))
            job_name = input("Enter Job Name: ")
            priority = int(input("Enter Priority (1 = High): "))

            scheduler.add_job(job_id, job_name, priority)

        # EXECUTE JOB
        elif choice == 2:
            scheduler.execute_job()

        # DISPLAY JOBS
        elif choice == 3:
            scheduler.display_jobs()

        # REMOVE JOB
        elif choice == 4:
            job_id = int(input("Enter Job ID to remove: "))
            scheduler.remove_job(job_id)

        # EXIT
        elif choice == 5:
            print("\nExiting Job Scheduler...")
            break

        else:
            print("\nInvalid choice! Please try again.")

    except ValueError:
        print("\nPlease enter valid input!")
