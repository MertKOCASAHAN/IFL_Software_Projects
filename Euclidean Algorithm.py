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
            let devam = true;

            while (devam) {
                let a = parseInt(prompt("Bir sayı giriniz:"));
                let b = parseInt(prompt("İkinci bir sayı giriniz:"));

                // Sonucu hemen yazdır
                let sonuc = OBEB(a, b);
                sonucDiv.innerHTML += `<p>OBEB(${a}, ${b}) = ${sonuc}</p>`;

                // Devam etmek isteyip istemediğini sor
                let cevap = prompt("Yeni işlem yapmak ister misiniz? (Evet/Hayır)").toLowerCase();
                if (cevap !== "evet") {
                    devam = false;
                }
            }
        }
    </script>
</body>
</html>


        


