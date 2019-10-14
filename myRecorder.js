var recorder;
var audio = document.querySelector('audio');
function blobToDataURL(blob, callback) {
    var a = new FileReader();
    a.onload = function (e) { callback(e.target.result); }
    a.readAsDataURL(blob);
}

function changeStatus(id_a, id_b) {
    var a = document.getElementById(id_a);
    var b = document.getElementById(id_b);
    temp = a.style.display;
    a.style.display = 'none';
    b.style.display = temp;
}

function startRecording(a, b) {
    HZRecorder.get(function (rec) {
        recorder = rec;
        recorder.start();
    });
    changeStatus(a, b)
}
function stopRecording(a, b) {
    recorder.stop();
    changeStatus(a, b);
    uploadAudio();
    // recorder.play(audio);
}

function playRecording() {
    recorder.play(audio);
}

function uploadAudio() {
    recorder.upload("https://lightspeech.xyz.:8080/", function (state, e) {
        switch (state) {
            case 'uploading':
                //var percentComplete = Math.round(e.loaded * 100 / e.total) + '%';
                break;
            case 'ok':
                //alert(e.target.responseText);
                // alert("上传成功");
                // window.location.href = "http://127.0.0.1:8000";
                break;
            case 'error':
                alert("上传失败");
                break;
            case 'cancel':
                alert("上传被取消");
                break;
        }
    });
}
