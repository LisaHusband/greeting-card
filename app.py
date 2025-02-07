from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cards.db'  # 使用 SQLite 数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 数据库模型
class GreetingCard(db.Model):
    id = db.Column(db.String(36), primary_key=True)  # 唯一ID
    background = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    font_color = db.Column(db.String(50), nullable=False)
    effect = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<GreetingCard {self.id}>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_card', methods=['POST'])
def generate_card():
    # 获取前端传来的数据
    background = request.form['background']
    text = request.form['text']
    font_color = request.form['font_color']
    effect = request.form['effect']

    # 创建唯一的ID
    card_id = str(uuid.uuid4())

    # 存储到数据库
    new_card = GreetingCard(
        id=card_id,
        background=background,
        text=text,
        font_color=font_color,
        effect=effect
    )
    db.session.add(new_card)
    db.session.commit()

    # 返回生成的链接
    return jsonify({'card_url': url_for('view_card', card_id=card_id, _external=True)})

@app.route('/card/<card_id>')
def view_card(card_id):
    card = GreetingCard.query.get_or_404(card_id)
    return render_template('card.html', card=card)

if __name__ == '__main__':
    with app.app_context():  # 在应用上下文中运行
        db.create_all()  # 创建数据库表
    app.run(debug=True)
