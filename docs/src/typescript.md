# JavaScript

```
function getRemoteImageAsBase64(url) {
  return new Promise((resolve, reject) => {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'arraybuffer';

    xhr.onload = function(e) {
      if (this.status == 200) {
        var ary = new Uint8Array(this.response);
        var i = ary.length;
        var binaryString = new Array(i);
        while (i--) {
          binaryString[i] = String.fromCharCode(ary[i]);
        }
        resolve(btoa(binaryString.join('')));
      } else {
        reject(this.response);
      }
    };

    xhr.send();
  });
}

let url = "https://example.com/foo";
audioData = await getRemoteImageAsBase64(url);
```
