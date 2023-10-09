function ForcePriority {

    param (
        $Process
    )

    $pr = Get-Process $Process -ErrorAction SilentlyContinue
    if ($pr){
        Write-Host "$Process is running at" $pr.PriorityClass
        $pr.PriorityClass = "AboveNormal"
    }
    else {
        Write-Output "$Process is NOT running"
    }
}

function PriorityAgent {
    param (
        $Process        
    )

    while (1 -eq 1)
    {
        ForcePriority $Process
        Start-Sleep -Seconds 5
    }
}
