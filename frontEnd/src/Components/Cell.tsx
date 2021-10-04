import React from 'react';

type CellContent = {
    itemName: string;
    description: string;
}

export default class Cell extends React.Component<CellContent> {
    constructor(props: CellContent) {
        super(props);
        this.state = {
            itemName: "",
            description: "",
        };
    }

    render() {
        return(
            <button
            className="cell"
            onClick={() => console.log("click")}
            >
                Box
            </button>
        );
    }
}
