from backend.database import sessionLocal
from backend import models
QUESTIONS = [
    {
        "order": 1,
        "text": "To start a class, do you",
        "options": [
    {"label":"A", "text": "Pose difficult questions to set the tone for the day?" , "primary_tag": "Student-Centered" ,"secondary_tag": "Assessment-Driven" },
    {"label":"B", "text": "Strike up a conversation/discussion?" , "primary_tag": "Student-Centered", "secondary_tag": "Inquiry"},
    {"label":"C", "text": "Go straight into the lecture notes?" , "primary_tag": "Teacher-Led", "secondary_tag": "High-Structure"}
]
    },
{
        "order": 2,
        "text": "Do you use instructional materials (slides, study aids, e.t.c.) in your classes?",
        "options": [
    {"label":"A", "text": "Yes" , "primary_tag": "Instrument-Assisted-Learning", "secondary_tag": None},
    {"label":"B", "text": "No" , "primary_tag": "High-Structure", "secondary_tag": None}
]
    },
{
        "order": 3,
        "text": "Your ideal classroom is",
        "options": [
    {"label":"A", "text": "Quiet and Introspective" , "primary_tag": "High-Structure" ,"secondary_tag": "Teacher-Led" },
    {"label":"B", "text": "Spontaneous(i.e. not the same from lecture to lecture)" , "primary_tag": "Flexible", "secondary_tag": "Student-Centered"},
    {"label":"C", "text": "A mix of both" , "primary_tag": "Student-Centered", "secondary_tag": "High-Structure"}
]
    },
{
        "order": 4,
        "text": "How do you decide pacing?",
        "options": [
    {"label":"A", "text": "By the lecture schedule created at the beginning" , "primary_tag": "High-Structure" ,"secondary_tag": None},
    {"label":"B", "text": "Through student feedback" , "primary_tag": "Student-Centered", "secondary_tag": "Flexible"},
    {"label":"C", "text": "Through student mastery of concepts" , "primary_tag": "Mastery-Based", "secondary_tag": "Flexible"},
    {"label":"D", "text": "Through assignments" , "primary_tag": "Assessment-Driven", "secondary_tag": "Flexible"}
]
    },
{
        "order": 5,
        "text": "How voluminous are your aassignments?",
        "options": [
    {"label":"A", "text": "Shallow (a few pages of work)" , "primary_tag": "Assessment-Driven" ,"secondary_tag": None},
    {"label":"B", "text": "Complex enough to count as a small project" , "primary_tag": "Project-Based", "secondary_tag": None},
]
    },
{
        "order": 6,
        "text": "How frequently do you give assignments?",
        "options": [
    {"label":"A", "text": "At the end of every lecture/Weekly" , "primary_tag": "Assessment-Driven" ,"secondary_tag": None},
    {"label":"B", "text": "At the end of every lesson topic/Bulky assignments" , "primary_tag": "Project-Based", "secondary_tag": None},
]
    },
{
        "order": 7,
        "text": "If many students struggle with a particular topic, you prefer to",
        "options": [
    {"label":"A", "text": "Reteach and practice" , "primary_tag": "MAstery-Based" ,"secondary_tag": "Teacher-Led" },
    {"label":"B", "text": "Change approach and solicit feedback" , "primary_tag": "Student-Centered", "secondary_tag": "Flexible"},
    {"label":"C", "text": "Use guided questions to point them in the right direction" , "primary_tag": "Inquiry", "secondary_tag": "Student-Centered"},
    {"label":"D", "text": "Encourage them to explore material outside of class with no other changes" , "primary_tag": "High-Structure", "secondary_tag": None}
]
    },
{
        "order": 8,
        "text": "The purpose of my assignments is",
        "options": [
    {"label":"A", "text": "Reinforcement through practice" , "primary_tag": "Teacher-Led" ,"secondary_tag": "Mastery-Based" },
    {"label":"B", "text": "Creative applications of concepts learnt in class" , "primary_tag": "Project-Based", "secondary_tag": None},
    {"label":"C", "text": "Reflection on learning" , "primary_tag": "Student-Centered", "secondary_tag": "Inquiry"},
]
    },
{
        "order": 9,
        "text": "Your lesson planning style is",
        "options": [
    {"label":"A", "text": "Detailed agenda" , "primary_tag": "High-Structure" ,"secondary_tag": None},
    {"label":"B", "text": "Framework + adapt" , "primary_tag": "Flexible", "secondary_tag": None},
    {"label":"C", "text": "Project Milestones" , "primary_tag": "Project-Based", "secondary_tag": None},
]
    },
{
        "order": 10,
        "text": "How do you handle classroom rules?",
        "options": [
    {"label":"A", "text": "Clear rules enforced consistently" , "primary_tag": "High-Structure" ,"secondary_tag": None},
    {"label":"B", "text": "Cocreated Norms" , "primary_tag": "Student-Centered", "secondary_tag": None},
    {"label":"C", "text": "Minimal rules, trust based" , "primary_tag": "Flexible", "secondary_tag": None},
]
    },
{
        "order": 11,
        "text": "Feedback on work done should be",
        "options": [
    {"label":"A", "text": "Fast + Specific + Rubic-based" , "primary_tag": "Assessment-Driven" ,"secondary_tag": "High-Structure" },
    {"label":"B", "text": "Iterative with revisions" , "primary_tag": "Mastery-Based", "secondary_tag": None},
    {"label":"C", "text": "Dialogue/Conference Style" , "primary_tag": "Student-Centered", "secondary_tag": "Inquiry"},
]
    },
{
        "order": 12,
        "text": "Student engagement comes from",
        "options": [
    {"label":"A", "text": "Clear Structure + Confidence" , "primary_tag": "High-Structure" ,"secondary_tag": None},
    {"label":"B", "text": "Choice + Relevance", "primary_tag": "Student-Centered", "secondary_tag": "Flexible"},
    {"label":"C", "text": "Challenge + Authentic Problems" , "primary_tag": "Project-Based", "secondary_tag": None},
]
    },
{
        "order": 13,
        "text": "How do you believe office hours should be set and enforced?",
        "options": [
    {"label":"A", "text": "Office hours should be the only time I attend to students outside the class" , "primary_tag": "High-Structure" ,"secondary_tag": None},
    {"label":"B", "text": "The hours are a bit mandatory but other times can be made available if needed" , "primary_tag": "Short-Office-Hours", "secondary_tag": "Flexible"},
    {"label":"C", "text": "I don't believe in or set office hours, I am always available" , "primary_tag": "Long-Office-Hours", "secondary_tag": "Student-Centered"},
]
    },
{
        "order": 14,
        "text": "Group work is",
        "options": [
    {"label":"A", "text": "Occasional and structured" , "primary_tag": "High-Structure" ,"secondary_tag": None},
    {"label":"B", "text": "Frequent and central" , "primary_tag": "Student-Centered", "secondary_tag": "Project-Based"},
    {"label":"C", "text": "Mostly optional" , "primary_tag": "Flexible", "secondary_tag": None},
]
    },
{
        "order": 15,
        "text": "Your ‘best class’ looks like",
        "options": [
    {"label":"A", "text": "Everyone meets the objective" , "primary_tag": "Mastery-Based" ,"secondary_tag": None},
    {"label":"B", "text": "Students ask great questions" , "primary_tag": "Inquiry", "secondary_tag": None},
    {"label":"C", "text": "Students build something meaningful" , "primary_tag": "Project-Based", "secondary_tag": None},
]
    },
]

def seed():
    db = sessionLocal()
    inserted_q = updated_q=inserted_o = updated_o = 0
    try:
        for q in QUESTIONS:
            order = q["order"]
            text = q["text"]
            question = db.query(models.Philosophy_Question).filter(models.Philosophy_Question.order == order).first()

            if question is None:
                question = models.Philosophy_Question(order = order, text = text)
                db.add(question)
                db.flush()
                inserted_q += 1
            else:
                if question.text != text:
                    question.text = text
                    updated_q += 1

            for opt in q["options"]:
                label = opt["label"]
                opt_row =db.query(models.Philosophy_Option).filter(models.Philosophy_Option.question_id == question.id, models.Philosophy_Option.label == label).first()
                if opt_row is None:
                    opt_row = models.Philosophy_Option(question_id=question.id, label=label, text = opt["text"], primary_tag = opt["primary_tag"], secondary_tag = opt["secondary_tag"])
                    db.add(opt_row)
                    inserted_o += 1
                else:
                    changed = False
                    if opt_row.text != opt["text"]:
                        opt_row.text = opt["text"]
                        changed = True
                    if getattr(opt_row, "primary_tag", None) != opt["primary_tag"]:
                        opt_row.primary_tag = opt["primary_tag"]
                        changed = True
                    if getattr(opt_row, "secondary_tag", None) != opt["secondary_tag"]:
                        opt_row.secondary_tag = opt["secondary_tag"]
                        changed = True
                    if changed:
                        updated_o += 1
        db.commit()
        print(f"Questions: inserted={inserted_q}, updated={updated_q}")
        print(f"Options: inserted={inserted_o}, updated={updated_o}")
    finally:
       db.close()

if __name__ == "__main__":
    seed()
