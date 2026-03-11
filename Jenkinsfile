pipeline {
    agent any

    environment {
        TOTAL_SHARDS = "3"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Distributed Tests') {
            matrix {
                axes {
                    axis {
                        name 'SHARD_INDEX'
                        values '0', '1', '2'
                    }
                }

                stages {

                    stage('Run Shard') {
                        steps {
                            sh """
                                echo "Running shard ${SHARD_INDEX}/${TOTAL_SHARDS}"

                                python3 -m venv venv_${SHARD_INDEX}
                                . venv_${SHARD_INDEX}/bin/activate

                                pip install --upgrade pip
                                pip install -r requirements.txt

                                playwright install

                                pytest tests \
                                    -n 3 \
                                    --dist loadscope \
                                    --shard-id=${SHARD_INDEX} \
                                    --num-shards=${TOTAL_SHARDS} \
                                    --junitxml=results_${SHARD_INDEX}.xml
                            """
                        }
                    }

                }

                post {
                    always {
                        junit "results_${SHARD_INDEX}.xml"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        failure {
            echo "Tests failed"
        }
    }
}