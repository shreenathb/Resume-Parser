import React, { useState } from 'react';
import axios from 'axios';

function NERDisplacy() {

    const [nerHTML, setNerHTML] = useState('');


    const handleAnalyze = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/ner');
            setNerHTML(response.data.html);
        } catch (error) {
            console.error('Error performing NER:', error);
        }
    };

    return (
        <div>
            <h2>Named Entity Recognition (NER) Visualization</h2>
            <button onClick={handleAnalyze}>Get results</button>

            {nerHTML && (
                <div
                    dangerouslySetInnerHTML={{ __html: nerHTML }}
                    style={{ marginTop: '20px', border: '1px solid #ccc', padding: '20px' }}
                />
            )}
        </div>
    );
}

export default NERDisplacy;