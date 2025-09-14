<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Öklid Algoritması - OBEB</title>
</head>
<body>
    <h1>Öklid Algoritması ile OBEB Hesaplama</h1>
    <div id="sonuc"></div>
    <button onclick="basla()">Başlat</button>

    <script>
        function OBEB(a, b) {
            while (b !== 0) {
                let temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }

        function basla() {
            let sonucDiv = document.getElementById("sonuc");

            function sor() {
                let a = parseInt(prompt("Bir sayı giriniz:"));
                let b = parseInt(prompt("İkinci bir sayı giriniz:"));
                let sonuc = OBEB(a, b);
                sonucDiv.innerHTML += `<p>OBEB(${a}, ${b}) = ${sonuc}</p>`;

                let devam = prompt("Devam etmek ister misiniz? (Evet/Hayır)").toLowerCase();
                if (devam === "evet") {
                    sor(); // Kendini tekrar çağırır
                }
            }

            sor(); // İlk çağrı
        }
    </script>
</body>
</html>

        

