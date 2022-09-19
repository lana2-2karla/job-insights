from src.jobs import read


def get_unique_job_types(path: str):
    jobs_list = read(path)
    job_type = [job["job_type"] for job in jobs_list]
    return list(set(job_type))


def filter_by_job_type(jobs: list, job_type: str):
    jobs_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_type


def get_unique_industries(path: str):
    jobs_list = read(path)
    job_type = [job["industry"] for job in jobs_list if job["industry"] != ""]
    return list(set(job_type))


def filter_by_industry(jobs, industry):
    jobs_type = [job for job in jobs if job["industry"] == industry]
    return jobs_type


def get_max_salary(path: str):
    jobs_list = read(path)
    job_type = [
        int(job["max_salary"])
        for job in jobs_list
        if job["max_salary"].isdigit()
    ]
    return max(job_type)


def get_min_salary(path):
    jobs_list = read(path)
    job_type = [
        int(job["min_salary"])
        for job in jobs_list
        if job["min_salary"].isdigit()
    ]
    return min(job_type)


def matches_salary_range(job, salary):
    is_min_salary = job.get("min_salary")
    is_max_salary = job.get("max_salary")

    if is_min_salary is None or is_max_salary is None:
        raise ValueError()
    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list
