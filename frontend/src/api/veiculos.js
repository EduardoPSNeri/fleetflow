import { apiRequest } from './api.js';

export function listarVeiculos() {
    return apiRequest('/veiculos/');
}