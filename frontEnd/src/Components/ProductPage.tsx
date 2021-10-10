import React from 'react';
import ReactDOM from 'react-dom';
import Item from './Item';
import { storeProducts } from '../TestData/data';
import { ItemConsumer } from './Context';

type Product = {
    itemName: string;
    description: string;
    link: string; // replace with Link from react router
}

type ProductProps = {
}

type ProductState = {
    products: Array<Product>;
}

export default class ProductPage extends React.Component<ProductProps, ProductState> {
    constructor(props: ProductProps) {
        super(props);
        this.state = {
            products: storeProducts,
        };
    }

    render(): JSX.Element {
        console.log(this.state.products);
        return (
            <div className="product">
                <div className="row">
                    <div className="item">
                        <ItemConsumer>
                        {item => {
                            return item.products.map(item => {
                                return <Item key={item.itemName} collectable={item}/>
                            })
                        }}
                    </ItemConsumer>
                    </div>
                </div>
            </div>
        );
    }

}
