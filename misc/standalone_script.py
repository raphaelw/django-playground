"""
Note: Execute this script with project root as PYTHONPATH (same path as manage.py)
in bash: `PYTHONPATH=. python misc/standalone_script.py`
alternative hack: python -m misc.stanalone_script
"""

from mysite import wsgi # init and load the full django project

# ---------- standalone script ----------
from polls.models import Question

latest_question_list = Question.objects.order_by("-pub_date")[:5]
output = ", ".join([q.question_text for q in latest_question_list])
print(output)

