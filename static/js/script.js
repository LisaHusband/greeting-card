console.log('Script loaded');

document.getElementById('generateBtn').addEventListener('click', function() {
    console.log('Button clicked');
    var background = document.getElementById('background').value;
    var text = document.getElementById('text').value;
    var fontColor = document.getElementById('font_color').value;
    var effect = "";

    // 更新预览
    var preview = document.getElementById('cardPreview');
    preview.style.backgroundColor = background;
    preview.style.color = fontColor;
    preview.innerHTML = `<p>${text}</p>`;

    if (effect === "heart") {
        preview.innerHTML += `<div class="heart-effect"></div>`;
    } else if (effect === "sparkle") {
        preview.innerHTML += `<div class="sparkle-effect"></div>`;
    }

    console.log('Sending request to the server');

    // 发送数据到后端生成贺卡
    fetch('/generate_card', {
        method: 'POST',
        body: new URLSearchParams({
            'background': background,
            'text': text,
            'font_color': fontColor,
            'effect': effect
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response received:', data);
        alert('贺卡生成成功！请分享链接: ' + data.card_url);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
