import { listarVeiculos } from './api/veiculos.js';

async function iniciar() {
    try {
        const veiculos = await listarVeiculos();

        console.log('Veículos:', veiculos);
    } catch (erro) {
        console.error('Erro:', erro.message);
    }
}

iniciar();