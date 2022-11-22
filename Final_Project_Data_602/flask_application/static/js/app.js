// Define function that will run on page load

function init() {

   // Read json data
    // Add dropdown option for each sample
    // data is an object with three arrays, names, metadata, and samples
    //let state_selector = d3.select("#selYearDataset");
    // let county_selector = d3.select("#selCountyDataset");

  d3.json("/year_list").then(function (data) {
    console.log(data);
    // rand_state=Math.floor(Math.random() * 48);
    let year_data = Object.values(data.year)
    
    // To read the values into an array
    console.log(year_data[0]);

    //Binding state array to the dropdown menu
    let select_year = document.getElementById('selYearDataset');
    for(var i = 0; i < year_data.length; i++) {
        var option = document.createElement('option');
        option.innerHTML = year_data[i];
        option.value = year_data[i];
        select_year.appendChild(option);
     }

    // Call functions below using the first sample to build Demographic and initial plots
  
    buildCharts(state_data[0])
  });
}
//--------------------------------------------------------------------------------------
// Define a function that will create charts for given sample
// Plotly Bar plot
function buildCharts(sampleYear) {

    console.log(sample)

    // Plotly Bar Chart:
    let barChart = d3.select("#bar");

    // Read the json data

    d3.json(`/covid_data/${sampleYear}`).then(function (data) {

        // console.log(Object.values(object1));
        // console.log(Object.values(data.state));
        // console.log(Object.values(data.below_hs_diploma_2019));
        let stateData = Object.values(data.state)
        let degree1Data = Object.values(data.total_cases)
        let degree2Data = Object.values(data.total_deaths) 

        var trace1 = {
            x: stateData,
            y: degree1Data,
            name: 'total_cases',
            type: 'bar'
            };
          
        var trace2 = {
            x: stateData,
            y: degree2Data,
            name: 'total_deaths',
            type: 'bar'
            };
        
        
        var data = [trace1, trace2];
          
        
        
        var layout = {
          title: {
            text:'Level of Education by State (Person_Count)',
            font: {
              family: 'Courier New, monospace',
              size: 18
            },
            xref: 'paper',
            x: 0.05,
          },
          
          yaxis: {
            title: {
              text: 'Population',
              font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              }
            }
          },
          barmode: 'stack'
        };

        // var layout = {barmode: 'stack'};
          
        Plotly.newPlot('bar', data, layout);      
    })
    //--------------------------------------------------------
    
}
    
//fuction buildCharts ends
//----------------------------------------------------------------------------------
function yearChanged(sample) {
  // The parameter being passed in this function is new sample id from dropdown menu
  console.log(sample)

  console.log(state_value)

  
  console.log(state_value) 

  let year_selector = document.getElementById('selYearDataset');
  console.log(year_selector.options[year_selector.selectedIndex].value)
  year_value = year_selector.options[year_selector.selectedIndex].value
  console.log(year_value)

  buildCharts(sample);  

} 

// Initialize dashboard on page load
init();
populateYear()
