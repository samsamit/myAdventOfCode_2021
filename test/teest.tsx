import React from 'react'

interface tool{
    material: string;
}
interface food{
    calorries: number;
}

interface item<T>{
    itemData: T; // What to do here?
    price: number;
}

interface IProps{
    inputItem: {
        [key: string]:{
            // Recodr type
        }
    }
}

const form = ({inputItem}: IProps) => {
    return (
        <div>
            <p></p>
            <p></p>
            <p></p>
            <p></p>
            <p></p>
            <p></p>
        </div>
    )
}

export default form
