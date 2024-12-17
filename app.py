from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageDraw
import io

app = Flask(__name__)


@app.route('/process-image', methods=['POST'])
def process_image():
    try:

        if 'image' not in request.files:
            return jsonify({"error": "Nenhuma imagem enviada"}), 400

        file = request.files['image']
        img = Image.open(file).convert("RGBA")


        width, height = img.size
        radius = 50  
        mask = Image.new("L", (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=255)

        img.putalpha(mask)  
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        return send_file(buffer, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
