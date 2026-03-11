pipeline {
    agent any
    stages {
        stage('Distributed Tests') {
            matrix {
                axes {
                    axis {
                        name 'SHARD_INDEX'
                        values '1', '2'
                    }
                }
                environment {
                    TOTAL_SHARDS = '2'
                }
                stages {
                    stage('Run Shard') {
                        steps {
                            sh """
                            rm -rf venv
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                            playwright install

                            # -n auto: pytest-xdist parallelization (Local CPUs)
                            # --shard: Playwright distribution (Across Jenkins nodes)
                            pytest -n auto --shard ${SHARD_INDEX}/${TOTAL_SHARDS} --junitxml=results_${SHARD_INDEX}.xml
                            """
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            // Aggregates all XML results from shards into one Jenkins report
            junit 'results_*.xml'
        }
    }
}
