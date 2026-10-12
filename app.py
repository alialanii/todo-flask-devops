from flask import Flask, jsonify, request

app = Flask(__name__)

# مصفوفة مؤقتة في الذاكرة لتخزين المهام (قاعدة بيانات مؤقتة)
tasks = [
    {"id": 1, "title": "تعلم أساسيات الـ DevOps", "done": False},
    {"id": 2, "title": "بناء أول تطبيق Flask", "done": True}
]

# 1. مسار لعرض جميع المهام (GET)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# 2. مسار لإضافة مهمة جديدة (POST)
@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json or not 'title' in request.json:
        return jsonify({"error": "Missing title"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json['title'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify({"task": new_task}), 201

# تشغيل التطبيق على المنفذ 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
