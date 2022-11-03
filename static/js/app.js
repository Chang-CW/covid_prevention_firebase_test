const result_text = document.querySelector('#result_text');
const result_proba = document.querySelector('#result_proba');
const result = document.querySelector('#result');

if (parseFloat(result_proba.innerText) >= 50.0) {
    result.classList.remove('d-none');
    result_text.classList.add('text-danger');
} else if (parseFloat(result_proba.innerText) < 50.0) {
    result.classList.remove('d-none');
    result_text.classList.add('text-success');
}