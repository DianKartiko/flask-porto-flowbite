from extensions import db
from datetime import datetime

# Tabel Asosiasi (Project <-> Skill)
project_skills = db.Table(
    "project_skills",
    db.Column("project_id", db.Integer, db.ForeignKey("project.id"), primary_key=True),
    db.Column("skill_id", db.Integer, db.ForeignKey("skill.id"), primary_key=True),
)


class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Skill {self.name}>"


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    link_demo = db.Column(db.String(200), nullable=True)
    link_repo = db.Column(db.String(200), nullable=True)

    # --- KOLOM TANGGAL PROJECT ---
    # 1. Tanggal manual (Kapan proyek selesai?)
    project_date = db.Column(db.Date, nullable=True)

    # 2. Tanggal sistem (Audit)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    skills = db.relationship(
        "Skill",
        secondary=project_skills,
        lazy="subquery",
        backref=db.backref("projects", lazy=True),
    )

    def __repr__(self):
        return f"<Project {self.title}>"
