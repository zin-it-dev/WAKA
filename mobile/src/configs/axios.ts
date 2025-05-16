import axios from 'axios';

const BASE_URL = 'http://192.168.1.11:8080/api/v1/';

const instance = axios.create({
	baseURL: BASE_URL,
	timeout: 10000,
	headers: {
		'Content-Type': 'application/json',
	},
});

export default instance;
