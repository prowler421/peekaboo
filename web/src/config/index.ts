const LOCAL_API_URL = 'http://localhost:8080';
export const API_URL = process.env.REACT_APP_API_URL ?? LOCAL_API_URL;

export const SITE_BUILD_INFO = process.env.REACT_APP_BUILD_INFO ?? 'v0.0.0-devel';
