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
                            python3 -m venv venv_${SHARD_INDEX}
                            . venv_${SHARD_INDEX}/bin/activate

                            pip install --upgrade pip
                            pip install -r requirements.txt

                            playwright install

                            pytest -n auto \
                              --shard-id=${SHARD_INDEX} \
                              --num-shards=${TOTAL_SHARDS} \
                              --junitxml=results_${SHARD_INDEX}.xml
                            """
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            junit 'results_*.xml'
        }
    }
}