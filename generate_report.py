import json
import os

def get_scenario_name(file_path):
    # Extract the path from "mappings/" onwards, and remove the .json extension
    return file_path.split('mappings' + os.path.sep)[1].replace('.json', '')

def get_request_conditions(request):
    conditions = []
    if 'queryParameters' in request:
        for param, value_dict in request['queryParameters'].items():
            if isinstance(value_dict, dict):
                for op, v in value_dict.items():
                    conditions.append(f"Query param '{param}' {op} '{v}'")
            else:
                # Handle cases where the value is not a dictionary, though this is not standard for WireMock
                conditions.append(f"Query param '{param}' has value '{value_dict}'")

    if 'bodyPatterns' in request:
        for pattern in request['bodyPatterns']:
            if 'equalToJson' in pattern:
                try:
                    # Try to parse the string to a dict for pretty printing
                    json_body = json.loads(pattern['equalToJson'])
                    conditions.append(f"Request body equals: {json.dumps(json_body, ensure_ascii=False, indent=2)}")
                except (json.JSONDecodeError, TypeError):
                    conditions.append(f"Request body equals: {pattern['equalToJson']}")
            elif 'matchesJsonPath' in pattern:
                conditions.append(f"Body matches JSONPath: `{pattern['matchesJsonPath']}`")
            # Add more body pattern types if necessary

    if not conditions:
        return "Любой запрос" # "Any request" in Russian

    return ", ".join(conditions)

def get_notes_from_scenario(scenario_name):
    if "service-unavailable" in scenario_name or "service_unavailable" in scenario_name:
        return "Проверка обработки недоступности внешнего сервиса"
    if "bad-request" in scenario_name or "bad_request" in scenario_name:
        return "Проверка валидации входных параметров"
    if "not-found" in scenario_name or "no_addresses" in scenario_name or "no_properties" in scenario_name or "no_objects" in scenario_name:
        return "Ответ соответствует бизнес-ошибке (данных нет)"
    if "found" in scenario_name or "one_address" in scenario_name or "single-property" in scenario_name or "one_object" in scenario_name or "multiple-properties" in scenario_name or "multiple-documents" in scenario_name or "two_addresses" in scenario_name or "two_objects" in scenario_name:
        return "Happy-path сценарий, полный корректный ответ"
    return "N/A"


def generate_report(files):
    report_lines = []
    report_lines.append("| № | Сценарий | Условие (входные данные) | Код ответа (HTTP) | Пример ответа (Response body) | Примечания |")
    report_lines.append("|---|---|---|---|---|---|")

    row_index = 1
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Skipping non-JSON file: {file_path}")
                continue

            mocks = data if isinstance(data, list) else [data]

            for mock_data in mocks:
                # Basic check if it's a wiremock mapping
                if not ('request' in mock_data and 'response' in mock_data):
                    continue

                scenario = get_scenario_name(file_path)
                if len(mocks) > 1:
                    # If there are multiple mocks in a file, append a unique identifier
                    if 'name' in mock_data:
                        scenario += f" ({mock_data['name']})"
                    else:
                        scenario += f" (item {mocks.index(mock_data) + 1})"


                request = mock_data.get('request', {})
                response = mock_data.get('response', {})

                conditions = get_request_conditions(request)
                http_code = response.get('status', 'N/A')

                response_body = ""
                if 'jsonBody' in response:
                    response_body = f"```json\n{json.dumps(response['jsonBody'], indent=2, ensure_ascii=False)}\n```"
                elif 'body' in response:
                    response_body = f"```\n{response['body']}\n```"
                elif 'bodyFileName' in response:
                    response_body = f"See file: {response['bodyFileName']}"

                notes = get_notes_from_scenario(scenario)

                report_lines.append(f"| {row_index} | {scenario} | {conditions} | {http_code} | {response_body} | {notes} |")
                row_index += 1


    return "\n".join(report_lines)

if __name__ == "__main__":
    files_to_process = []
    for root, _, files in os.walk("wiremock/mappings"):
        for file in files:
            if file.endswith(".json"):
                files_to_process.append(os.path.join(root, file))

    report = generate_report(sorted(files_to_process))

    with open("report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("Report generated successfully: report.md")
