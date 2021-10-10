import React from 'react';
import { Link } from 'react-router-dom';

type ItemProps = {
    collectable: {
        itemName: string,
        description: string,
        link: string,
    }
}

export default class Item extends React.Component<ItemProps> {
    constructor(props: ItemProps) {
        super(props);
    }

    render(): JSX.Element {
        // Replace image with actual image link
        return (
            <div>
                <h1>Collectable</h1>
                <img src="https://www.pinclipart.com/picdir/middle/565-5658340_transparent-testing-clipart-free-test-clipart-png.png" />
                <h3>{this.props.collectable.itemName}</h3>
                <p>{this.props.collectable.description}</p>
                <a href={this.props.collectable.link}>Link</a>
            </div>
        )
    }
}
