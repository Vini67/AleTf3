from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
    {"id": 1, "titulo": "Primeiro Post", "conteudo": "Olá mundo"}
]

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/api/posts", methods=["GET"])
def listar_posts():
    return jsonify(posts)

@app.route("/api/posts/<int:id>", methods=["GET"])
def get_post(id):
    for post in posts:
        if post["id"] == id:
            return jsonify(post)
    return {"erro": "Post não encontrado"}, 404

@app.route("/api/posts", methods=["POST"])
def criar_post():
    data = request.json
    novo = {
        "id": len(posts)+1,
        "titulo": data["titulo"],
        "conteudo": data["conteudo"]
    }
    posts.append(novo)
    return jsonify(novo)

app.run(host="0.0.0.0", port=5000)