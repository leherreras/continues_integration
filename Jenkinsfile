node("CI") {
    if (env.BRANCH_NAME == 'master') {
        PROJECT_NAME = env.JOB_NAME.replaceAll('\\/' + env.JOB_BASE_NAME, '').replaceAll("_", "-")
        try{
            stage("Getting from Git") {
                echo "[STEP] This is a test of clone git"
                checkout scm
            }

            stage("Valid version"){
                templateVersion=sh(script: 'git diff --name-only  HEAD^ HEAD | grep version', returnStdout:true)
                if(templateVersion) {
                    echo "[INFO] All is well"
                }else {
                    echo "[ERROR] The version has not been modified"
                    throw new Exception("The version has not been modified")
                }
            }

            stage("Turning Docker services off"){
                    echo "[STEP] Down docker services"
                    sh 'docker-compose down --rmi=local'

            }

            stage("Building Docker"){
                echo "[STEP] Building the docker containers"
                sh 'docker-compose up --build -d'
            }

            stage("Sanity check docker"){
                echo "[STEP] Run script to review up the service"
                sh "sh verify.sh"
            }


            stage("Running unittest"){
                echo "[INFO] Running unittest"
                sh "python test/test_main.py"
            }

            stage("QA manual verification") {

                 timeout(time: 1, unit: 'DAYS'){
                     input message: 'Verification finished?',
                           parameters: [[$class: 'BooleanParameterDefinition',
                                         defaultValue: false,
                                         description: 'Ticking this box will gives the verification done',
                                         name: 'Done']]
                 }
            }
         }catch(e)
        {
            currentBuild.result = "FAILED"
            echo "[STEP] Down docker services"
            sh 'docker-compose down --rmi=local'
            throw e
        }
    }
}