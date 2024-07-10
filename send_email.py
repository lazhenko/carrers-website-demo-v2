from mailjet_rest import Client
import os

api_key = os.environ['MAIL_JET_API_KEY']
api_secret = os.environ['MAIL_JET_SECRET_KEY']

mailjet = Client(auth=(api_key, api_secret), version='v3.1')


def send_email_to_applicant(applicant_email: str, job:dict, full_name):
  html_part = f"""
          <body>
          <p>Dear {full_name},</p>
          <p>Thank you for your interest in the {job['title']} position at Fearsome. We appreciate you taking the time to submit your application through our web portal.</p>
          <p>We have received a high volume of applications for this role and are currently in the process of reviewing them carefully.</p>
          <h2>Here's what to expect next:</h2>
          <ul>
            <li>If you are shortlisted for an interview, we will contact you within 3 business days to schedule a time to speak with you.</li>
          <p>We appreciate your patience and understanding throughout this process.</p>
          <p>Sincerely,</p>
          <p>The Fearsome Team</p>
      </body>"""
  custom_id = f"Application for {job['title']} Submitted"
  data = {
      'Messages': [{
          "From": {
              "Email": "lazhenko.artem@gmail.com",
              "Name": "Artem"
          },
          "To": [{
              "Email": applicant_email,
              "Name": full_name
          }],
          "Subject": "Your application at Fearsome Careers",
          "TextPart": "Thanks for your application",
          "HTMLPart": html_part,
          "CustomID": custom_id
      }]
  }
  result = mailjet.send.create(data=data)
