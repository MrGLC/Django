# Use the SDK image to build the application
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["YourProject.csproj", "./"]
RUN dotnet restore "./YourProject.csproj"
COPY . .
RUN dotnet publish "YourProject.csproj" -c Release -o /app/publish

# Use the runtime image to run the application
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "YourProject.dll"]

