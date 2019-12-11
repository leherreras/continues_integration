node() {
    if (env.BRANCH_NAME == 'master') {
        PROJECT_NAME = env.JOB_NAME.replaceAll('\\/' + env.JOB_BASE_NAME, '').replaceAll("_", "-")

            stage("Getting from Git") {
                echo "[STEP] This is a test of clone git"
                checkout scm
            }

//            stage("Valid version"){
//                templateVersion=sh(script: 'git diff --name-only  origin/master | grep version', returnStdout:true)
//                sh "git diff --name-only  origin/master | grep version"
//                if(templateVersion) {
//                    echo "[INFO] All is well"
//                }else {
//                    echo "[ERROR] The version has not been modified"
//                    throw new Exception("The version has not been modified")
//                }
//            }

            stage("Turning Docker services off"){
                try{
                    echo "[STEP] Down docker services"
                    sh 'docker-compose down --rmi=local'
                }catch(e)
                {
                    currentBuild.result = "FAILED"
                    throw e
                }
            }

            stage("Building Docker"){
                echo "[STEP] Building the docker containers"
                sh 'docker-compose up --build -d'
            }

            stage("Sanity check docker"){
                echo "[STEP] Run script to review up the service"
                sh "sh verify.sh"
            }


            stage("Running functional test"){
                echo "[INFO] Running functional test"
            }

            stage("QA Verification") {

                 timeout(time: 1, unit: 'DAYS'){
                     input message: 'Verification finished?',
                           parameters: [[$class: 'BooleanParameterDefinition',
                                         defaultValue: false,
                                         description: 'Ticking this box will gives the verification done',
                                         name: 'Done']]
                 }
            }
        }


    }
}