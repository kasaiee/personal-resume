import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from ...models import (
    Profile,
    Experience,
    Education,
    Project,
    Skill,
)


class Command(BaseCommand):
    help = "Create fake users with resume data quickly"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=50,
            help="Number of users to create",
        )

    def handle(self, *args, **options):
        choice = input('Do you want to DELETE EXISTING USERS? (Y/n)')
        if choice == 'Y':
            User.objects.all().delete()

        count = options["count"]

        fake = Faker()

        # --------------------------------------------------
        # Data
        # --------------------------------------------------

        job_titles = [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Python Developer",
            "Django Developer",
            "Software Engineer",
            "Web Developer",
            "Data Analyst",
            "UI/UX Designer",
            "DevOps Engineer",
        ]

        companies = [
            "Tech Company",
            "Software Solutions",
            "Digital Agency",
            "Startup Inc.",
            "Web Studio",
            "IT Solutions",
        ]

        positions = [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Python Developer",
            "Django Developer",
            "Software Engineer",
        ]

        universities = [
            "University of Toronto",
            "University of British Columbia",
            "University of Melbourne",
            "University of Amsterdam",
            "University of Manchester",
            "Technical University of Munich",
            "University of California",
            "University of Washington",
        ]

        degrees = [
            "diploma",
            "associate",
            "bachelor",
            "master",
            "phd",
        ]

        fields_of_study = [
            "Computer Science",
            "Software Engineering",
            "Information Technology",
            "Computer Engineering",
            "Information Systems",
            "Data Science",
        ]

        project_titles = [
            "E-commerce Platform",
            "Task Management App",
            "Portfolio Website",
            "Social Media Platform",
            "Job Board",
            "Learning Management System",
            "Real Estate Platform",
            "Online Booking System",
        ]

        available_skills = [
            "Python",
            "Django",
            "JavaScript",
            "TypeScript",
            "React",
            "HTML",
            "CSS",
            "Git",
            "Docker",
            "PostgreSQL",
            "MySQL",
            "REST API",
        ]

        interests = [
            "Programming",
            "Reading",
            "Photography",
            "Traveling",
            "Gaming",
            "Music",
            "Technology",
            "Football",
            "Hiking",
            "Writing",
        ]

        # --------------------------------------------------
        # Generate Users
        # --------------------------------------------------

        users = []

        for _ in range(count):
            first_name = fake.first_name()
            last_name = fake.last_name()

            username = (
                f"{first_name.lower()}."
                f"{last_name.lower()}."
                f"{random.randint(100000, 999999)}"
            )

            users.append(
                User(
                    username=username,
                    email=fake.unique.email(),
                    password="pbkdf2_sha256$720000$test$test",
                    first_name=first_name,
                    last_name=last_name,
                )
            )

        # Bulk insert users
        users = User.objects.bulk_create(
            users,
            batch_size=1000,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(users)} users"
            )
        )

        # --------------------------------------------------
        # Generate Profiles
        # --------------------------------------------------

        profiles = []

        for user in users:
            profiles.append(
                Profile(
                    user=user,
                    phone=fake.phone_number(),
                    job_title=random.choice(job_titles),
                    description=fake.paragraph(
                        nb_sentences=4
                    ),
                    intrests=", ".join(
                        random.sample(
                            interests,
                            k=random.randint(3, 5),
                        )
                    ),
                    location=f"{fake.city()}, {fake.country()}",
                )
            )

        Profile.objects.bulk_create(
            profiles,
            batch_size=1000,
        )

        # --------------------------------------------------
        # Generate Experiences
        # --------------------------------------------------

        experiences = []

        for user in users:

            experience_count = random.randint(1, 3)

            for _ in range(experience_count):
                experiences.append(
                    Experience(
                        user=user,
                        title=random.choice(companies),
                        location=f"{fake.city()}, {fake.country()}",
                        date_range=random.choice([
                            "2021 - 2022",
                            "2022 - 2023",
                            "2023 - 2024",
                            "2024 - Present",
                            "2022 - Present",
                        ]),
                        position=random.choice(positions),
                        job_description=fake.paragraph(
                            nb_sentences=3
                        ),
                    )
                )

        Experience.objects.bulk_create(
            experiences,
            batch_size=1000,
        )

        # --------------------------------------------------
        # Generate Education
        # --------------------------------------------------

        educations = []

        for user in users:

            education_count = random.randint(1, 2)

            for _ in range(education_count):
                educations.append(
                    Education(
                        user=user,
                        university=random.choice(universities),
                        location=fake.city(),
                        date_range=random.choice([
                            "2016 - 2020",
                            "2017 - 2021",
                            "2018 - 2022",
                            "2019 - 2023",
                            "2020 - 2024",
                        ]),
                        degree=random.choice(degrees),
                        study_description=random.choice(
                            fields_of_study
                        ),
                    )
                )

        Education.objects.bulk_create(
            educations,
            batch_size=1000,
        )

        # --------------------------------------------------
        # Generate Projects
        # --------------------------------------------------

        projects = []

        for user in users:

            project_count = random.randint(1, 4)

            for _ in range(project_count):
                projects.append(
                    Project(
                        user=user,
                        title=random.choice(project_titles),
                        description=fake.paragraph(
                            nb_sentences=4
                        ),
                    )
                )

        Project.objects.bulk_create(
            projects,
            batch_size=1000,
        )

        # --------------------------------------------------
        # Generate Skills
        # --------------------------------------------------

        skills = []

        for user in users:

            skill_count = random.randint(5, 8)

            selected_skills = random.sample(
                available_skills,
                k=skill_count,
            )

            for skill_name in selected_skills:
                skills.append(
                    Skill(
                        user=user,
                        title=skill_name,
                        level=random.randint(1, 5),
                    )
                )

        Skill.objects.bulk_create(
            skills,
            batch_size=1000,
        )

        # --------------------------------------------------
        # Done
        # --------------------------------------------------

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "========================================"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Fake resume data created successfully!"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Users:        {len(users)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Profiles:     {len(profiles)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Experiences:  {len(experiences)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Education:    {len(educations)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Projects:     {len(projects)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Skills:       {len(skills)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "========================================"
            )
        )