function saveResults() {
    const data = {
        name: userName,
        score: score.toFixed(2),
        incorrect: incorrect
    };

    fetch('/save-result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === 'success') {
            alert('Results saved successfully.');
        } else {
            alert('There was an error saving your results.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error saving your results.');
    });
}
