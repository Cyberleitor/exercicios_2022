const modoTerror = 'dark-mode';
const h1 = document.getElementById('page-title');
const button = document.getElementById('mode-selector');
const footer = document.getElementById('pezinho');
const body = document.getElementById('corpo');

button.addEventListener('click', luzAlternando)

function luzAlternando() {
    acenderApagar();
    apagarAcender();
}

function acenderApagar() {
    h1.classList.toggle(modoTerror);
    button.classList.toggle(modoTerror);
    footer.classList.toggle(modoTerror);
    body.classList.toggle(modoTerror);
}

function apagarAcender() {
    const luzAcesa = 'Ligar';
    const luzApagada = 'Desligar';

    if (body.classList.contains(modoTerror)) {
        button.innerHTML = luzAcesa;
        h1.innerHTML = 'Ficou com medo? Eu ouvi passos! Acenda a luz!';
        return;
    }

    button.innerHTML = luzApagada;
    h1.innerHTML = 'Você tem coragem de apagar a luz?';
}