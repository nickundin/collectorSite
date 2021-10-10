import React from 'react';
import { storeProducts } from '../TestData/data';

type ItemProps = {
    children: React.ReactNode;
}

type ItemState = {
    products: Array<ItemData>
}

type ItemData = {
    itemName: string;
    description: string;
    link: string; // change to link later
}

type ItemContextType = [
    ItemData[], React.Dispatch<React.SetStateAction<ItemData[]>>
];

const ItemContext = React.createContext({} as ItemState);

class ItemProvider extends React.Component<ItemProps, ItemState> {
    constructor(props: ItemProps) {
        super(props);
        this.state = {
            products: storeProducts
        }
    }
    render(): JSX.Element {
        return(
            <ItemContext.Provider value={{
                ...this.state
            }}>
                {this.props.children}
            </ItemContext.Provider>
        );
    }
}

const ItemConsumer = ItemContext.Consumer;

export { ItemProvider, ItemConsumer };
