import React from 'react';
import { Switch, Route } from 'react-router-dom';
import HomePage from './HomePage';
import NotFoundPage from './NotFoundPage';
import CommunityPage from './CommunityPage';
import ProductPage from './ProductPage';

export default function Routing(): JSX.Element {
    return (
        <Switch>
            <Route exact path="/" component={HomePage} />
            <Route exact path="/community" component={CommunityPage} />
            <Route exact path="/products" component={ProductPage} />
            <Route component={NotFoundPage} />
        </Switch>
    );
}
