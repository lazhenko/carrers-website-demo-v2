import os
from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.datastructures import ImmutableMultiDict

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
	with engine.connect() as conn:
		result = conn.execute(text("select * from jobs"))
	
		jobs = []
	for row in result.all():
		jobs.append(row._asdict())
	return jobs

def load_job_from_db(id):
	with engine.connect() as conn:
		result = conn.execute(
			text("SELECT * FROM jobs WHERE id = :val"), {"val":id}
		)
		rows = result.all()
		if len(rows) == 0:
			return None
		else:
			return rows[0]._asdict()


def add_application_to_db(job_id:int, data: ImmutableMultiDict):
	try:
			with engine.begin() as conn:
					query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
					query_params = {
							'job_id': job_id,
							'full_name': data['full_name'],
							'email': data['email'],
							'linkedin_url': data['linkedin_url'],
							'education': data['education'],
							'work_experience': data['work_experience'],
							'resume_url': data['resume_url']
					}
					result = conn.execute(query, query_params)
					return result.rowcount > 0
	except SQLAlchemyError as e:
			print(f"An error occurred: {e}")
			return False