// You are driving on a circular road with N gas stations on it. Each gas station has a limited
// amount of gas it can give you, specified by the input array A. The gas cost to the next gas station
// varies, and is specified by the input array B.
//
// We want to see whether it is possible to do a full loop of the road, filling up at each station.
// This might be impossible, or it might only be possible for some starting stations. Determine the
// lowest index station which allows us to complete a full loop, ending up where we began.

fn gas_station_loop(gas_amounts: &[u32], gas_costs: &[u32]) -> Option<usize> {
    assert_eq!(gas_amounts.len(), gas_costs.len());
    let n = gas_amounts.len();
    // Determine how much gas is spent at each leg.
    let diffs: Vec<i32> = gas_amounts.iter().zip(gas_costs.iter()).map(|(a, b)| (*a as i32 - *b as i32)).collect();
    // Track the cumulative amount of gas in the tank.
    let tank: Vec<i32> = diffs.iter().scan(0, |sum, x| {
        *sum += x;
        Some(*sum)
    }).collect();
    if *tank.last().expect("not empty") < 0 {
        return None  // Not enough gas to complete a loop.
    }
    // Start the journey just after the lowest point.
    let (min_index, _) = tank.iter().enumerate().min_by_key(|(_, &gas)| gas).expect("not empty");
    let starting_station = (min_index + 1) % n;
    Some(starting_station)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gas_station_loop() {
        let test_cases = vec![
            (vec![2], vec![3], None),
            (vec![1, 1, 1, 1], vec![0, 1, 5, 1], None),
            (vec![2], vec![1], Some(0)),
            (vec![1, 2], vec![2, 1], Some(1)),
            (vec![0, 0, 5, 0, 0], vec![1, 1, 1, 1, 1], Some(2)),
            (vec![1, 1, 1, 1, 1], vec![0, 0, 5, 0, 0], Some(3)),
            (vec![0, 3, 0, 3], vec![3, 0, 3, 0], Some(1)),
            (vec![0, 3, 0, 3], vec![3, 0, 3, 0], Some(1)),
        ];
        for (gas_amounts, gas_costs, idx) in test_cases {
            assert_eq!(
                gas_station_loop(&gas_amounts, &gas_costs),
                idx,
                "gas_station_loop({:?}, {:?}) != {:?}",
                gas_amounts, gas_costs, idx
            );
        }
    }
}
