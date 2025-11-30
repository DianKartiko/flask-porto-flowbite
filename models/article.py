from extensions import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    # --- KOLOM TANGGAL ARTIKEL ---
    # 1. Tanggal manual (Kapan artikel diterbitkan?)
    published_date = db.Column(db.Date, default=datetime.utcnow)

    # 2. Tanggal sistem (Audit)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Article {self.title}>"
