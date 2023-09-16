#!/usr/bin/env pwsh
#Requires -Version 5.0
Get-DnsClientCache | Export-Csv -Path '.\stuff.csv'
