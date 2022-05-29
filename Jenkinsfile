properties([pipelineTriggers([pollSCM('* * * * * ')])])
node {
    stage("clone") {
        git "https://github.com/omerk14/Devops1004.git"
    }
    stage("show files"){
        bat "dir"
    }
}
