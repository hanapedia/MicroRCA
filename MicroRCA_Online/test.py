import requests
import time
import argparse


def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='Root cause analysis for microservices')

    # parser.add_argument('--folder', type=str, required=False,
    #                     default='1',
    #                     help='folder name to store csv file')
    
    parser.add_argument('--length', type=int, required=False,
                    default=150,
                    help='length of time series')

    parser.add_argument('--step', type=str, required=False,
                    default='14s',
                    help='length of step')
    # parser.add_argument('--url', type=str, required=False,
    #                 default='http://localhost:9090/api/v1/query',
    #                 help='url of prometheus query')

    return parser.parse_args()

if __name__ == '__main__':
    metric_step = '14s'
    args = parse_args()

    # folder = args.folder
    len_second = args.length
    prom_url = 'http://localhost:31090/api/v1/query_range'

    end_time = time.time()
    start_time = end_time - len_second
    # start_time = "2022-09-07 10:14:05"
    # end_time = "2022-09-07 10:24:05"
    query = 'histogram_quantile(0.50, sum(irate(istio_request_duration_miliseconds_bucket{reporter="source", destination_workload_namespace="sock-shop"}[1m])) by (destination_workload, source_workload, le))'
    response = requests.get(prom_url,
                            params={'query': query,
                                # 'time': time,})
                                    'start': start_time,
                                    'end': end_time,
                                    'step': metric_step})
    print(response.json())
