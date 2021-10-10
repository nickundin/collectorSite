import React from 'react';
import { Link } from 'react-router-dom';

export default function NotFoundPage(): JSX.Element {
    return(
        <div>
            <h1>404 Not Found</h1>
            <Link to="/">Return home</Link>
        </div>
    );
}
